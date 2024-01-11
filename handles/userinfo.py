# userinfo.py
class UserInfo:
    @staticmethod
    def get_user_info(user):
        # Implement detailed logic to retrieve user information
        roles = ', '.join([role.name for role in user.roles])
        joined_at = user.joined_at.strftime('%Y-%m-%d %H:%M:%S') if user.joined_at else 'Not available'
        created_at = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        
        return f'User Info: {user.name}, {user.id}\n' \
               f'Roles: {roles}\n' \
               f'Joined Server at: {joined_at}\n' \
               f'Account Created at: {created_at}'
