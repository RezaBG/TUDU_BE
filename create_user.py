from src.services.dependencies import get_db
from src.services.task import get_password_hash
from src.models.user import User

def create_admin_user():
    db = next(get_db())
    hashed_password = get_password_hash("admin")
    admin_user = User(
        username="admin",
        email="admin@example.com",
        hashed_password=hashed_password,
        is_admin=True,
        disabled=False
    )
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    print(f"Admin user created: {admin_user.username}")

create_admin_user()
