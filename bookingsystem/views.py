from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import GuestBooking
from .forms import BookingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Restaurant home page class, renders the page in the browser


class Home (generic.ListView):
    model = GuestBooking
    template_name = 'index.html'


# The get request returns the template as above
def get(self, request):
    return render(request, 'base.html')


# class allowing menu page to be rendered in the browser 


class Menu(generic.DetailView):
    def get(self, request):
        return render(request, 'menu.html')

# class for the thank you page to be rendered in the browser


class Thankyou(generic.DetailView):
    def get(self, request):
        return render(request, 'thankyou.html')



# This class will allow the user to create their booking (bookings are being made)

class MakeBooking(generic.CreateView):
    model = GuestBooking
    template_name = 'make_booking.html'
    form_class = BookingForm
    
    def get_success_url(self):
        return reverse('thankyou')

    def booking_add(request):
        if request.method == 'POST':
            if form.is_valid:
                booking = form.save()
                booking.user = request.user
                booking.save()
            return redirect('thankyou')
        else:
            form = BookingForm()
            context = {'form': form}
            return render(request, 'make_booking.html', context)



# View bookings made on the my_booking page

def ViewBooking(request):
    bookings = GuestBooking.objects.filter()
    context = {'bookings': bookings}
    return render(request, 'my_booking.html', context)


# This class will allow for the user to edit a booking

class BookingEdit(generic.UpdateView):
    model = GuestBooking
    fields = ['guest', 'day', 'time']
    template_name = 'edit_booking.html'
    success_url = 'my_booking'


# This class will allow for the user to delete their booking 
 
class BookingDelete(generic.DeleteView):
    model = GuestBooking
    template_name = 'delete_booking.html'
    success_url = 'my_booking'
