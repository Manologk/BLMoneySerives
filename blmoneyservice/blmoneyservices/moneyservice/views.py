from django.shortcuts import render, redirect
from .moneytransferalgo import Variablez
from users.models import Client, Transaction, TransactionDetails

import random


# def homepage(request):
#     print(request.POST)
#     return render(request, 'moneyservice/home.html', )


amountRus_Zam = 0
amountZam_Rus = 0
resRus_Zam = ()
resZam_Rus = ()
algo = Variablez()

# change these variables
usd_Rub_Buying = 60
usd_Rub_Selling = 59
zmw_usd_buying = 17
zmw_usd_selling = 16.5


def homepage(request):
    global amountRus_Zam, amountZam_Rus, resRus_Zam, resZam_Rus
    if request.method == 'POST':
        amountRus_Zam = request.POST['amount']
        amountZam_Rus = request.POST['amountzmw']
        resRus_Zam = algo.rub2kwacha(float(amountRus_Zam), usd_Rub_Buying, zmw_usd_selling)
        resZam_Rus = algo.kwacha2rub(float(amountZam_Rus), zmw_usd_buying, usd_Rub_Selling)
        transaction = Transaction(trans_type="Rus-Zam", amount=amountRus_Zam)
        transaction.save()
        return redirect(get_details_rus_zam)

    return render(request, 'moneyservice/home.html')


def get_details_rus_zam(request):
    global amountRus_Zam, resRus_Zam
    # if request.method == 'POST':


    return render(request, 'moneyservice/recipientDetailsRUS_ZAM.html', {
        'amount': amountRus_Zam,
        'commission': resRus_Zam[2],
        'total': resRus_Zam[3]
    })


def display_transaction_rus_zam(request):
    global amountRus_Zam, resRus_Zam
    print(request.POST)
    return render(request, 'moneyservice/transferRus_Zam.html', {'amount': amountRus_Zam})


def transaction_id():
    pass