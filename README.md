# Web UI Test With Python Behave
>*libraries* Behave, Selenium

</br>

  **Feature: Test**</br>
    Web UI Tests with Python Behave</br>
</br>

  **Scenario: verify login**</br>
    *Given* navigate to website</br>
    *And* close the address selection</br>
    *When* open sign in page</br>
    *And* enter email "*email*" and password "*password*"</br>
    *Then* verify homepage is open</br>
</br>

![test1](https://user-images.githubusercontent.com/88919177/151692957-6ebc8b3f-1f5e-4ba3-ad3c-94a575f49621.gif)

</br>

  **Scenario: verify empty basket**</br>
    *Given* navigate to website</br>
    *And* close the address selection</br>
    *When* search for "Lale"</br>
    *And* filter "kırmızı" color ones</br>
    *And* select the first product</br>
    *And* add product to basket</br>
    *And* delete product from the basket</br>
    *Then* verify homepage is open</br>
</br>

![test2](https://user-images.githubusercontent.com/88919177/151693023-831930ba-7093-4a40-93ff-adef8762d269.gif)
