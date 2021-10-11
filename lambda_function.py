### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta
from botocore.vendored import requests

### Functionality Helper Functions ###
def parse_float(n):
    """
    Securely converts a non-numeric value to float.
    """
    try:
        return float(n)
    except ValueError:
        return float("nan")




def get_fg_index():
    """
    Retrieves the current Bitcoin Fear & Greed Index from the alternative.me Crypto API.
    """
    fgi_url = "https://api.alternative.me/fng/"
    response = requests.get(fgi_url)
    response_json = response.json()
    fg_index = parse_float(response_json["data"][0]["value"])
    return fg_index


def get_watson():
    watson_ = ""
    response_w = requests.get(watson_)
    response_json_w =  response_w.json()
    watson_index = parse_float(reponse_json_w["data"][0]["value"])
    return watson_index

def get_vader():
    vader = ""
    response_v = requests.get(vader)
    reponse_json_v = response_v.json()
    vader_index = parse_float(response_json_v["data"][0]["value"])
    return vader_index

def get_blob():
    blob = ""
    response_b = requests.get(blob)
    reponse_json_b = response_b.json()
    blob_index = parse_float(response_json_b["data"][0]["value"])
    return blob_index

def get_recommendation():
    """
    Returns a buying recommendation based on the current value of the Bitcoin Fear & Greed Index.
    """
    fg_index = get_fg_index()
    recommendation = ""
    if fg_index >= 0 and fg_index <=25:
        recommendation = "Be cautious on buying bitcoin today since the market feels 'Extreme Fear'."
    elif fg_index > 25 and fg_index < 50:
        recommendation = "Be cautious on buying bitcoin today since the market feels 'Fear'."
    elif fg_index == 50:
        recommendation = "You may buy bitcoin today since the market feels 'Neutral'."
    elif fg_index > 50 and fg_index <= 75:
        recommendation = "You may buy bitcoin today, the market feels 'Greed'"
    else:
        recommendation = "You may buy bitcoin today, the market feels 'Extreme Greed'"
    return recommendation


def get_watson_recommendation():
    watson_index=get_watson()
    watson_score = ""
    if watson_index >=0 and watson_index <= 40:
        watson_score = "Sentiment is negative", watson_score
    elif watson_index > 40 and watson_index < 60:
        watson_score = "Sentiment is neutral", watson_score
    else:
        watson_score = "Sentiment is positive", watson_score
        
def get_vader_recommendation():
    vader_index=get_vader()
    vader_score = ""
    if vader_index >=0 and vader_index <= 40:
        vader_score = "Sentiment is negative", vader_score
    elif vader_index > 40 and vader_index < 60:
        vader_score = "Sentiment is neutral", vader_score
    else:
        vader_score = "Sentiment is positive", vader_score


def get_blob_recommendation():
    blob_index=get_blob()
    blob_score = ""
    if blob_index >=0 and blob_index <= 40:
        blob_score = "Sentiment is negative", blob_score
    elif blob_index > 40 and blob_index < 60:
        blob_score = "Sentiment is neutral", blob_score
    else:
        blob_score = "Sentiment is positive", blob_score
        
        

def build_validation_result(is_valid, violated_slot, message_content):
    """
    Defines an internal validation message structured as a python dictionary.
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




### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    # Get the name of the current intent
    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "getFGIndex":
        return convert_dollars(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
