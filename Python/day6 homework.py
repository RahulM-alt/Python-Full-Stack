blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

total_views = 0
trending_blog = 0

for views in blog_views:
    if  views > 1000:
        print("Trending")
        trending_blog += 1
    elif views >= 500 and views <= 1000:
        print("Average")
    else: 
        print("Low Traffic")
        total_views += views 

print("Total number of views:", total_views) 
print("Number of trending posts:", trending_blog)