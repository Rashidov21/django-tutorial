from .models import Post, Tags, Category


def view_all(request):
	context = {
		'recent_post':Post.objects.all().order_by('-id')[:3],
		'categories':Category.objects.all(),
		'tags':Tags.objects.all().order_by('-id')[:10]
		#order_by - korsatilgan paramettr boyicha saralash
	}
	return context