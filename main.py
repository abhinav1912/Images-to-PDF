import os
from PIL import Image
FILE_SIZE_LIMIT = 7*1024*1024
AUTHOR = "20020570007"


def convert(images, ques_number):
    n = len(images)
    if AUTHOR:
        final_file = f'Question_{ques_number}_RollNo_{AUTHOR}.pdf'
    else:
        final_file = f'Question_{ques_number}.pdf'
    try:
        im1 = Image.open(images[0]).convert('RGB')
        extra_images = []
        for i in range(1, n):
            extra_images.append(Image.open(images[i]).convert('RGB'))
        im1.save(final_file, save_all=True, append_images=extra_images)
        file_size = "%.2f" % (os.path.getsize(final_file)/(1024*1024))
        print(f"{final_file} created! (size = {file_size} Mb)")
    except Exception as e:
        print(e)


def main(questions, pages_per_question, cover_page=None, question_numbers = None):
    assert len(pages_per_question) == questions   # valid set of inputs

    files = sorted(
        [i for i in os.listdir() if (len(i) > 4 and i != cover_page) and (i[-4:] == ".png" or (i[-5:] == ".jpeg" or i[-4:] == ".jpg"))]
    )

    if cover_page:
        assert cover_page in os.listdir()

    assert sum(pages_per_question) == len(files)  # else missing pages

    if question_numbers:
        assert len(pages_per_question) == len(question_numbers)

    ctr = 0
    ques_count = 1
    for i in pages_per_question:
        if cover_page:
            current_set = [cover_page]+files[ctr:ctr+i]
        else:
            current_set = files[ctr:ctr+i]
        if question_numbers:
            question_number = question_numbers[ques_count-1] if question_numbers else ques_count

        convert(current_set, question_number)
        ctr += i
        ques_count += 1


if __name__ == '__main__':
    main(3, [2,3,2], cover_page="cover.jpeg", question_numbers=[1,2,6])
