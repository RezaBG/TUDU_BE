from src.services.dependencies import get_db
from src.services.task import get_password_hash
from src.models.user import User
from sqlalchemy import or_

def create_admin_user():
    db = next(get_db())
    print(f"Database session created: {db}")

    # Check if the user already exists
    username = "admin1"
    email = "admin1@example.com"
    existing_user = db.query(User).filter(or_(User.email == email, User.username == username)).first()
    if existing_user:
        print(f"A user with the email '{email}' or username 'admin' already exists.")
        return

    # Proceed to create the admin user if the email does't exist
    hashed_password = get_password_hash("admin")
    print(f"Hashed password: {hashed_password}")

    admin_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        is_admin=True,
        disabled=False
    )
    print(f"Admin user created: {admin_user}")

    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    print(f"Admin user created successfully: {admin_user.username}")

create_admin_user()
