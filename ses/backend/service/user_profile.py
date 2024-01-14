from ses.schemas.schemas import UserProfile
from ses.core.repository import MongoRepo

class UserProfileService:
    def __init__(self):
        self.repo = MongoRepo(
            UserProfile,
            "mongodb://localhost:27017",
            "ses"
        )

    def get_user_profile_by_email(self, email: str) -> UserProfile:
        return self.repo.get_by({"email": email})

    def add_user_profile(self, user_profile: UserProfile):
        self.repo.add(user_profile)