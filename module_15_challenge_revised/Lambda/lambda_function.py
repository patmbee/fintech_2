### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


"""
Step 3: Enhance the Robo Advisor with an Amazon Lambda Function
In this section, you will create an Amazon Lambda function that will validate the data provided by the user on the Robo Advisor.
1. Start by creating a new Lambda function from scratch and name it `recommendPortfolio`. Select Python 3.7 as runtime.
2. In the Lambda function code editor, continue by deleting the AWS generated default lines of code, then paste in the starter code provided in `lambda_function.py`.
3. Complete the `recommend_portfolio()` function by adding these validation rules:
    * The `age` should be greater than zero and less than 65.
    * The `investment_amount` should be equal to or greater than 5000.
4. Once the intent is fulfilled, the bot should respond with an investment recommendation based on the selected risk level as follows:
    * **none:** "100% bonds (AGG), 0% equities (SPY)"
    * **low:** "60% bonds (AGG), 40% equities (SPY)"
    * **medium:** "40% bonds (AGG), 60% equities (SPY)"
    * **high:** "20% bonds (AGG), 80% equities (SPY)"
> **Hint:** Be creative while coding your solution, you can have all the code on the `recommend_portfolio()` function, or you can split the functionality across different functions, put your Python coding skills in action!
5. Once you finish coding your Lambda function, test it using the sample test events provided for this Challenge.
6. After successfully testing your code, open the Amazon Lex Console and navigate to the `recommendPortfolio` bot configuration, integrate your new Lambda function by selecting it in the “Lambda initialization and validation” and “Fulfillment” sections.
7. Build your bot, and test it with valid and invalid data for the slots.
"""
def validate_data(first_name, age, investment_amount, risk_level, intent_request):
    # first name must be only letters    
    if first_name is not None:
        if not first_name.isalpha():
            return build_validation_result(False, 'firstName', "First name can only be letters. Please type again.")
        
    # The `age` should be greater than zero and less than 65.
    if age is not None:
        age = parse_int(age)
        if age <= 0:
            return build_validation_result(False, 'age', "Please enter a positive age younger than 65.")
        elif age >= 65:
            return build_validation_result(False, 'age', "Sorry only investors younger than 65 may use this service.")
      
    # The `investment_amount` should be equal to or greater than 5000.
    if investment_amount is not None:
        investment_amount = parse_int(investment_amount)
        is_investment_amount_valid = investment_amount >= 5000
        if not is_investment_amount_valid:
            violatedSlot = "investmentAmount"
            message = "Investment must be at least $5,000." 
            return build_validation_result(is_investment_amount_valid, violatedSlot, message)

    # Only allows risk levels from None, Low, Medium or High
    if risk_level is not None:       
        if not risk_level.lower() in ['none', 'low', 'medium', 'high']:
            violatedSlot = "riskLevel"
            message = "Valid risk levels include only None, Low, Medium or High." 
            return build_validation_result(False, violatedSlot, message)

    return build_validation_result(True, None, None)

# Used for the risk levels 
def investment_recommendation(risk_level):
    recommendation_result = ''
    if risk_level.lower()  == 'none':
        recommendation_result = '100% bonds (AGG), 0% equities (SPY)'
    elif risk_level.lower()  == 'low':
        recommendation_result = '60% bonds (AGG), 40% equities (SPY)'
    elif risk_level.lower()  == 'medium':
        recommendation_result = '40% bonds (AGG), 60% equities (SPY)'
    elif risk_level.lower()  == 'high':
        recommendation_result = '20% bonds (AGG), 80% equities (SPY)'
    return recommendation_result
    
### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    input_first_name = get_slots(intent_request)["firstName"]
    input_age = get_slots(intent_request)["age"]
    input_investment_amount = get_slots(intent_request)["investmentAmount"]
    input_risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]
    

 
    if source == 'DialogCodeHook':
        slots = get_slots(intent_request)
        validation_result = validate_data(input_first_name, input_age, input_investment_amount, input_risk_level, intent_request)
     
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(intent_request['sessionAttributes'],
                intent_request['currentIntent']['name'],
                slots, 
                validation_result['violatedSlot'],
                validation_result['message'])
        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
        return delegate(output_session_attributes, get_slots(intent_request))
  
    recommendation_result = investment_recommendation(input_risk_level)
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Given your risk level - {}. We recommend this investment: {}. Thank you, {}, for using RoboAdvisor. '.format(input_risk_level, recommendation_result, input_first_name)})

### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "recommendPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    return dispatch(event)