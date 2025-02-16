import instaloader

def fetch_instagram_profile(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        print("\n" + "="*50)
        print(f"Username        : {profile.username}")
        print(f"Full Name       : {profile.full_name}")
        print(f"Biography       : {profile.biography if profile.biography else 'No bio available'}")
        print(f"Profile Pic URL : {profile.profile_pic_url}")
        print(f"Posts Count     : {profile.mediacount}")
        print(f"Followers       : {profile.followers}")
        print(f"Following       : {profile.followees}")
        print(f"Private Account : {'Yes' if profile.is_private else 'No'}")
        print(f"Verified        : {'Yes' if profile.is_verified else 'No'}")
        print(f"External URL    : {profile.external_url if profile.external_url else 'No external link'}")
        print(f"Business Category: {profile.business_category_name if profile.business_category_name else 'Not a business account'}")
        
        # Display recent post caption if the account is public
        if not profile.is_private:
            print("\nRecent Post Caption:")
            for post in profile.get_posts():
                caption = post.caption if post.caption else "No caption"
                print(f"- {caption[:100]}...")  # Show first 100 characters
                break  # Fetch only the latest post
        else:
            print("\nCannot fetch posts. The profile is private.")

    except instaloader.exceptions.ProfileNotExistsException:
        print("❌ Error: The profile does not exist!")
    except instaloader.exceptions.InstaloaderException:
        print("❌ Error: Could not retrieve profile information. Please try again later.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

# Infinite loop for checking multiple users
while True:
    username = input("\nEnter Instagram Username (or type 'exit' to quit): ").strip()
    if username.lower() == 'exit':
        print("Exiting the script. Goodbye!")
        break
    fetch_instagram_profile(username)
