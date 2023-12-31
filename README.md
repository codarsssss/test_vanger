# Тестовое задание: Создание страницы по макету

## Задача
Необходимо создать новую страницу согласно макету [Figma](https://www.figma.com/file/csU67B0SQVZO1AkwvMZa3D/Тестовое-задание-N2?type=design&node-id=1-1012&mode=design&t=wz2qpqpXo6RochwT-0) с использованием следующих технологий и инструментов:

- Python 3.9
- Django 4.1
- MySQL
- Bootstrap 5
- [Slick Slider](http://kenwheeler.github.io/slick/) для реализации слайдера
- [django-filer](https://pypi.org/project/django-filer/) для работы с изображениями
- [django-admin-sortable2](https://pypi.org/project/django-admin-sortable2/) для сортировки записей в админке

#### Шаги для выполнения задачи:

1. **Сборка проекта:**
   - Использовать Python 3.9 для сборки проекта.
   - Django 4.1 и MySQL будут использоваться в качестве фреймворка и базы данных соответственно.

2. **Размещение проекта в Git репозитории:**
   - Создать Git репозиторий для проекта.
   - Закоммитеть исходный код и все необходимые файлы.

3. **Прописать логику:**
   - Прописать маршруты и представления.
   - Подготовить модели для хранения путей к файлам по id и title.
   - Подготовить формы для дальнейшего использования в админке

4. **Использовать Bootstrap 5 для клиентской части:**
   - Использовать Bootstrap 5 для стилизации и разметки страницы.
   - Применить дизайн из макета Figma.

5. **Использовать Slick Slider:**
   - Интегрировать Slick Slider для реализации слайдера.
   - Слайдер должен поддерживать функциональность Slider Syncing, как указано в макете.

6. **Открытие фотографий на весь экран:**
   - Реализовать функциональность открытия фотографий на весь экран по клику на большую фотографию в слайдере.
   - Обеспечить "листание" галереи в полноэкранном режиме.

7. **Настройка админки Django:**
   - Использовать django-filer для управления изображениями в слайдере через админку Django.
   - Настройка визуально понятный admin.py с отображением картинки и названия в списке записей элементов слайдера.

8. **Сортировка записей слайдера с использованием drag&drop:**
   - Использовать django-admin-sortable2 для реализации сортировки записей слайдера при помощи drag&drop в админке.

9. **Зависимости проекта:**
   - Создайте файл req.pip в корне проекта, содержащий все необходимые зависимости для запуска проекта.
