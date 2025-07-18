from django.shortcuts import render, get_object_or_404
from .models import BlogPost, GalleryImage
from django.utils import timezone

def index(request):
    # Get published blog posts
    blog_posts = BlogPost.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:3]
    
    # Get active gallery images
    gallery_images = GalleryImage.objects.filter(
        is_active=True
    ).order_by('order')[:8]  # Get first 8 ordered images
    
    context = {
        'blog_posts': blog_posts,
        'gallery_images': gallery_images,
    }
    return render(request, 'news/index.html', context)

def news_media(request):
    blog_posts = BlogPost.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:3]
    return render(request, 'news/news_media.html', {'blog_posts': blog_posts})

def press_releases(request):
    return render(request, 'news/press_releases.html')

def blog(request):
    blog_posts = BlogPost.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    return render(request, 'news/blog.html', {'blog_posts': blog_posts})

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'news/post_detail.html', {'post': post})

def events(request):
    return render(request, 'news/events.html')

# If you need a dedicated gallery page later:
def gallery(request):
    gallery_images = GalleryImage.objects.filter(is_active=True).order_by('order')
    return render(request, 'news/gallery.html', {'gallery_images': gallery_images})