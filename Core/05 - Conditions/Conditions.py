'''
    Python'da koşullar (conditions) if, elif ve else anahtar kelimeleri ile sağlanır.
    Conditions in Python are provided by if, elif and else keywords.

    Bu anahtar kelimelerin kullanımı şu şekildedir:
    The usage of these keywords is as follows:

    if condition:
        # This block is executed if the condition is met
    elif condition:
        # This block is executed if the first condition is not met and this condition is met
    else:
        # This block is executed if the conditions above are not met

    if koşul:
        # Koşul sağlanırsa burası çalışır
    elif koşul:
        # İlk koşul sağlanmazsa ve bu koşul sağlanırsa burası çalışır
    else:
        # Yukarıdaki koşullar sağlanmazsa burası çalışır

    Koşulların sağlanıp sağlanmadığını kontrol etmek için ==, !=, >, <, >=, <= operatörleri kullanılır.
    Conditions are checked with ==, !=, >, <, >=, <= operators.

    Bu operatörlerin kullanımı şu şekildedir:
    The usage of these operators is as follows:

        == : Eşitse
        == : Equal

        != : Eşit değilse
        != : Not equal

        >  : Büyükse
        >  : Greater than

        <  : Küçükse
        <  : Less than

        >= : Büyük veya eşitse
        >= : Greater than or equal to

        <= : Küçük veya eşitse
        <= : Less than or equal to

    Örnekler:
    Examples:
        1 == 1 : True
        1 != 1 : False
        1 > 1  : False
        1 < 1  : False
        1 >= 1 : True
        1 <= 1 : True

    Koşulların birleştirilmesi için and, or ve not anahtar kelimeleri kullanılır.
    Conditions are combined with and, or and not keywords.

    Bu anahtar kelimelerin kullanımı şu şekildedir:
    The usage of these keywords is as follows:

        and : İki koşul da sağlanırsa
        and : If both conditions are met

        or  : İki koşuldan biri sağlanırsa
        or : If one of the conditions is met

        not : Koşul sağlanmazsa
        not : If the condition is not met

    Örnekler:
    Examples:
            1 == 1 and 2 == 2 : True
            1 == 1 or 2 == 3  : True
            not 1 == 1        : False

    Koşulların birleştirilmesi için parantezler kullanılabilir.
    Parentheses can be used to combine conditions.

    Örnekler:
    Examples:
        (1 == 1 or 2 == 2) and 3 == 3 : True
        (1 == 1 or 2 == 3) and 3 == 3 : False
'''