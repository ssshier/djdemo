class AppCode:
    TYPEAPP = "01"


class MoudleCode:
    USER = "01"


class UserCMMap:
    _PREFIX = AppCode.TYPEAPP + MoudleCode.USER

    PASSWORD_MUST_MATCH = {
        "code": _PREFIX + "01",
        "message": "Password must match",
        "zh_message": "密码必须匹配",
    }
    PASSWORD_MUST_DIFF = {
        "code": _PREFIX + "02",
        "message": "New password must be different than old password",
        "zh_message": "新密码必须与旧密码不同",
    }


class CMMap:

    USER = UserCMMap
