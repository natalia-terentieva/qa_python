# qa_python


##### test_add_new_book_add_book_with_different_names_lengths_should_add_only_correct_name_length
*Тест добавляет книги с разной длиной названия. Будет добавлена только книга с корректной длиной названия.* 
Тестируемые методы: 
* add_new_book
* get_books_genre

##### test_add_new_book_add_book_with_the_same_name
*Тест добавляет 2 раза книгу с одним и тем же названием. Книга будет добавлена только один раз.*
Тестируемые методы: 
* add_new_book
* get_books_genre

##### test_set_book_genre_set_genre_scifi
*Тест добавляет книгу и устанавливает ей жанр 'Фантастика'. Будет добавлена 1 книга с жанром 'Фантастика'.*
Тестируемые методы: 
* add_new_book
* set_book_genre
* get_books_genre

##### test_set_book_genre_set_not_exist_genre
*Тест добавляет книгу и устанавливает ей несуществующий в списке жанр. Жанр у добавленной книги не изменится.*
Тестируемые методы: 
* add_new_book
* set_book_genre
* get_books_genre

##### test_get_books_with_specific_genre_get_all_genres
*Тест проверяет количество книг по каждому жанру. Количество должно соответствовать ожидаемому.*
Тестируемые методы: 
* get_books_with_specific_genre

##### test_get_books_for_children_two_book_for_adult_two_book_for_children
*Тест проверяет количество книг, подходящих для детей. Должно соответствовать 8.*
Тестируемые методы: 
* get_books_for_children

##### test_add_book_in_favorites_add_two_book_in_favorites
*Тест добавляет книги в Избранное. 2 раза добавляет одну и ту же книгу, книга должна добавиться один раз.*
Тестируемые методы: 
* add_book_in_favorites
* get_list_of_favorites_books

##### test_add_book_in_favorites_not_existing_book_should_not_add_to_favorites
*Тест добавляет в Избранное несуществующую книгу. Книга не будет добавлена*
Тестируемые методы: 
* add_book_in_favorites
* get_list_of_favorites_books

##### test_delete_book_from_favorites_delete_one_book
*Тест добавляет и удаляет книги из Избранного. В Избранном должна остаться только неудаленная книга.*
Тестируемые методы: 
* add_book_in_favorites
* get_list_of_favorites_books
* delete_book_from_favorites
