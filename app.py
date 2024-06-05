from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def get_bot_response():
    user_input = request.form['msg']
    #mocking the response here, this will be an actual request to whatever LLM
    response = {"response": str(send_bot_request())}
    return jsonify(response)
    #bot_response = chatbot.get_response(user_input)
    #return jsonify(response=str(bot_response))

def send_bot_request():
    # do the request
    return '''{
  "order": {
    "amountOfMoney": {
      "currencyCode": "EUR",
      "amount": 2980
    },
    "customer": {
      "merchantCustomerId": "mc_{{TIMESTAMP}}",
      "personalInformation": {
        "name": {
          "title": "Mr.",
          "firstName": "Wile",
          "surnamePrefix": "E.",
          "surname": "Coyote"
        },
        "gender": "male",
        "dateOfBirth": "19490917"
      },
      "companyInformation": {
        "name": "Acme Labs"
      },
      "languageCode": "en",
      "billingAddress": {
        "street": "Desertroad",
        "houseNumber": "13",
        "additionalInfo": "b",
        "zip": "84536",
        "city": "Monument Valley",
        "state": "Utah",
        "countryCode": "US"
      },
      "shippingAddress": {
        "name": {
          "title": "Miss",
          "firstName": "Road",
          "surname": "Runner"
        },
        "street": "Desertroad",
        "houseNumber": "1",
        "additionalInfo": "Suite II",
        "zip": "84536",
        "city": "Monument Valley",
        "state": "Utah",
        "countryCode": "US"
      },
      "contactDetails": {
        "emailAddress": "wile.e.coyote@acmelabs.com",
        "phoneNumber": "+1234567890",
        "faxNumber": "+1234567891",
        "emailMessageType": "html"
      },
      "vatNumber": "1234AB5678CD"
    },
    "references": {
      "merchantOrderId": "{{TIMESTAMP}}",
      "merchantReference": "mr_{{TIMESTAMP}}",
      "invoiceData": {
        "invoiceNumber": "0005400123",
        "invoiceDate": "20140306191500"
      },
      "descriptor": "Fast and Furry-ous"
    },
    "typeInformation": {
      "purchaseType": "physical"
    },
    "shoppingCart": {
      "items": [
        {
          "amountOfMoney": {
            "currencyCode": "EUR",
            "amount": 2500
          },
          "invoiceData": {
            "description": "ACME Super Outfit"
          },
          "orderLineDetails": {
            "productName": "ACME12",
            "discountAmount": 0,
            "lineAmountTotal": 2500,
            "productCode": "ASO45",
            "productPrice": 500,
            "productType": "CLOTH",
            "quantity": 5,
            "taxAmount": 0,
            "unit": "piece"
          }
        },
        {
          "amountOfMoney": {
            "currencyCode": "EUR",
            "amount": 480
          },
          "invoiceData": {
            "description": "Asperin"
          },
          "orderLineDetails": {
            "productName": "ASPIRIN",
            "discountAmount": 0,
            "lineAmountTotal": 480,
            "productCode": "ASP01",
            "productPrice": 480,
            "productType": "MEDIC",
            "quantity": 1,
            "taxAmount": 0,
            "unit": "piece"
          }
        }
      ]
    }
  },
  "hostedCheckoutSpecificInput": {
    "returnUrl": "https://secure.ogone.com/ncol/test/displayparams.asp",
    "locale": "en_GB"
  },
  "CardPaymentMethodSpecificInput": {
    "PaymentProductId": 1,
    "RequiresApproval": true,
    "SkipAuthentication": true,
    "SkipFraudService": true
  }
}
}'''

if __name__ == "__main__":
    app.run(debug=True, port=8888)