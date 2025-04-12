from django.shortcuts import render
from django.http import JsonResponse
from nltk.corpus import wordnet
import nltk
import re

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


def simple_tokenizer(text):
    return re.findall(r'\b\w+\b', text.lower())

def chatbot_response(user_input):
    tokens = simple_tokenizer(user_input.lower())

    
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!",
        "what is your name": "I am a assistant bot! How can I help you?",
        "what do you do": "I can help you with product info, orders, tracking, returns, and more!",
        "how to place an order": "Just browse products, add them to your cart, and proceed to checkout!",
        "how to track my order": "You can track your order from the 'My Orders' section or give me your order ID.",
        "how to cancel my order": "You can cancel an order from your account before it's shipped, or I can help with that here.",
        "what is your return policy": "We offer easy 7-day returns on most products. Would you like to know about a specific item?",
        "do you offer free shipping": "Yes, we offer free shipping on orders above ₹499!",
        "how to contact support": "You can reach out to our customer support via chat, email, or call. I'm here to help too!",
        "what are your payment options": "We accept credit/debit cards, UPI, net banking, and Cash on Delivery.",
        "do you have any offers": "Yes! Check out our latest deals in the Offers section or let me know what you're shopping for.",
        "how do I apply a coupon": "You can enter your coupon code during checkout to get a discount.",
        "is COD available": "Yes, Cash on Delivery is available on most items unless stated otherwise.",
        "how to return a product": "Go to 'My Orders', select the item, and choose 'Return'. I can also guide you through it.",
        "how can I track my order": "Please provide your order number (e.g., #123456), and I’ll check the status for you.",
        "where is my order": "If you share your order ID, I can tell you exactly where it is!",
        "how can I return a product": "Sure! Just give me your order number and the reason for the return. I’ll guide you through the process.",
        "how long do returns take": "Once we receive your item, it usually takes 3–5 business days to process the return and refund.",
        "can I cancel my order": "Orders can be cancelled if they haven't shipped yet. Share your order number, and I’ll check for you.",
        "I received the wrong item": "Sorry about that! Please send us a photo of the product at support@example.com along with your order ID.",
        "how can I contact customer support": "You can email us at support@example.com or call our helpline at +91-9876543210. I'm also here to help!",
        "do you have Cash on Delivery": "Yes, Cash on Delivery (COD) is available on most items across India.",
        "is it safe to pay online": "Absolutely! We use 128-bit SSL encryption for secure payments.",
        "do you offer discounts or promo codes": "Yes! You can find the latest promo codes on our homepage or I can send one to your email.",
        "how do I reset my password": "Go to the login page and click 'Forgot Password'. We'll email you a reset link.",
        "my payment failed": "Sorry about that! Can you try again using a different method or contact support@example.com with your order details?"
        
    }

    
    synonym_dict = {
        "hello": ["hi", "hey", "greetings", "howdy", "hola"],
        "how are you": ["how's it going", "how do you do", "how are you doing", "what's up", "how's life", "how are things"],
        "bye": ["goodbye", "see you", "take care", "bye bye", "later"],
        "what is your name": ["what's your name", "who are you", "what should I call you"],
        "what do you do": ["what can you do", "what is your job", "what's your purpose", "what's your function"],
        "how to place an order": ["order something", "buy a product", "shop online", "purchase items"],
        "how to track my order": ["track order", "where is my order", "order status", "find my package"],
        "how to cancel my order": ["cancel order", "remove order", "stop order", "undo order"],
        "what is your return policy": ["return rules", "how to return", "can I return", "return instructions"],
        "do you offer free shipping": ["free delivery", "shipping charges", "no shipping fee", "is shipping free"],
        "how to contact support": ["customer support", "help center", "get help", "reach support"],
        "what are your payment options": ["how to pay", "payment methods", "ways to pay", "available payment options"],
        "do you have any offers": ["discounts", "promo codes", "deals", "special offers"],
        "how do I apply a coupon": ["use coupon", "add promo code", "apply discount code", "enter coupon"],
        "is COD available": ["cash on delivery", "cod option", "pay on delivery", "can I pay with cash"],
        "how to return a product": ["return product", "send item back", "product return process", "initiate return"],
        "I received the wrong item": ["wrong product", "incorrect delivery", "received wrong thing", "not what I ordered"],
        "how can I contact customer support": ["how to reach support", "talk to support", "contact service", "email support"]
    }


   
    normalized_input = " ".join(tokens)

    if normalized_input in responses:
        return responses[normalized_input]
    
   
    for key, synonyms in synonym_dict.items():
        if any(synonym in normalized_input for synonym in synonyms):
            return responses[key]

   
    return "Sorry, I didn't understand that. Can you rephrase?"


def chat(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "")
        response = chatbot_response(user_input)
        return JsonResponse({"response": response})
    
    return render(request, "bot/chat.html")











