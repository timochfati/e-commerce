{"filter":false,"title":"views.py","tooltip":"/checkout/views.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":120,"column":143},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","","from django.contrib.auth.decorators import login_required","","from django.contrib import messages","","from .forms import MakePaymentForm, OrderForm","","from .models import OrderLineItem","","from django.conf import settings","","from django.utils import timezone","","from products.models import Product","","import stripe","","","","# Create your views here.","","stripe.api_key = settings.STRIPE_SECRET","","","","","","@login_required()","","def checkout(request):","","    if request.method == \"POST\":","","        order_form = OrderForm(request.POST)","","        payment_form = MakePaymentForm(request.POST)","","","","        if order_form.is_valid() and payment_form.is_valid():","","            order = order_form.save(commit=False)","","            order.date = timezone.now()","","            order.save()","","","","            cart = request.session.get('cart', {})","","            total = 0","","            for id, quantity in cart.items():","","                product = get_object_or_404(Product, pk=id)","","                total += quantity * product.price","","                order_line_item = OrderLineItem(","","                    order=order,","","                    product=product,","","                    quantity=quantity","","                )","","                order_line_item.save()","","            ","","            try:","","                customer = stripe.Charge.create(","","                    amount=int(total * 100),","","                    currency=\"EUR\",","","                    description=request.user.email,","","                    card=payment_form.cleaned_data['stripe_id']","","                )","","            except stripe.error.CardError:","","                messages.error(request, \"Your card was declined!\")","","            ","","            if customer.paid:","","                messages.error(request, \"You have successfully paid\")","","                request.session['cart'] = {}","","                return redirect(reverse('products'))","","            else:","","                messages.error(request, \"Unable to take payment\")","","        else:","","            print(payment_form.errors)","","            messages.error(request, \"We were unable to take a payment with that card!\")","","    else:","","        payment_form = MakePaymentForm()","","        order_form = OrderForm()","","    ","","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE"]}],[{"start":{"row":120,"column":143},"end":{"row":121,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":120,"column":143},"end":{"row":120,"column":144},"action":"insert","lines":["}"],"id":5}],[{"start":{"row":120,"column":144},"end":{"row":120,"column":145},"action":"insert","lines":[")"],"id":6}],[{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"remove","lines":["    "],"id":7}]]},"ace":{"folds":[],"scrolltop":154,"scrollleft":0,"selection":{"start":{"row":121,"column":0},"end":{"row":121,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1564182241563,"hash":"6b200bd2d8b6384a2e4f2009e868f646cf6d21af"}