
from .models import  *
def test(request):
    context = {
        "one":Machine.objects.get(id=37),
        "withFilter":Student.objects.filter()
    }
    return context