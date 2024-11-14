

def f():
    raise ExceptionGroup(
            "group1",
            [
                OSError(1),
                SystemError(2),
                ExceptionGroup(
                    "group2",
                    [
                        OSError(3),
                        RecursionError(4)
                        ]
                    )
                ]
            )

try:
    f()
except* OSError as e:
    print("许多OSErrors错误")

except* SystemError as e:
    print("许多系统错误(SystemError)")

#3.12才支持的
