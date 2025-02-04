import instaloader

loader = instaloader.Instaloader()
post_url = "https://www.instagram.com/p/DDydlR_SYQG/?igsh=NXMwNmtqd2cybml1"  
post_id = post_url.split("/")[-2]  
loader.download_post(instaloader.Post.from_shortcode(loader.context, post_id), target="downloads")
print("Download complete!")