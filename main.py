import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Định nghĩa các model với các tỷ lệ khác nhau
models = {
    '0.2': keras.models.load_model('model_0.2.h5'),
    '0.4': keras.models.load_model('model_0.4.h5'),
    '0.6': keras.models.load_model('model_0.6.h5'),
    '0.8': keras.models.load_model('model_0.8.h5'),
    '1.0': keras.models.load_model('model_1.0.h5')
}


def run_model(model, input_text):
    # Chuẩn bị input text
    input_text = tf.convert_to_tensor([input_text], dtype=tf.string)

    # Dự đoán
    output = model.predict(input_text)

    # In kết quả
    print('Output:', output)


def main():
    while True:
        print('Chọn model:')
        print('0.2')
        print('0.4')
        print('0.6')
        print('0.8')
        print('1.0')
        print('e: thoát')

        choice = input('Nhập lựa chọn: ')

        if choice == 'e':
            break
        elif choice in models:
            model = models[choice]
            while True:
                input_text = input('Nhập văn bản hoặc "c" để tiếp tục: ')
                if input_text == 'c':
                    break
                run_model(model, input_text)
        else:
            print('Lựa chọn không hợp lệ. Vui lòng chọn lại.')


if __name__ == '__main__':
    main()
