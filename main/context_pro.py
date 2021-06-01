from .models import Post, Tags


def view_all(request):
	context = {
		'recent_post':Post.objects.all().order_by('-id')[:3],
		'tags':Tags.objects.all().order_by('-id')[:10]
		#order_by - korsatilgan paramettr boyicha saralash
	}
	return context