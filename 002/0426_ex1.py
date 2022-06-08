def average_media(a, b, c):
    a_weight = a * 3.5
    b_weight = b * 7.5
    c_weight = c * 8.0
    media = round(((a_weight + b_weight + c_weight) / 19), 5)

    print(f"""
        {a}
        {b}
        {c}
        MEDIA = {media}
        """)


if __name__ == '__main__':
    average_media(3.5, 7.5, 8)
