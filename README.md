
# setup

rename `.env.sample` into `.env`

# install

``` bash
pip install -r requirements.txt
```

# usage

``` bash
streamlit run app.py                              # run locally
```

# production

``` bash
heroku create wagon-streamlit-auth --region eu    # create heroku app
git push heroku master                            # push to production
```

Go to the **Settings** of your heroku app:
- click **Reveal Config Vars**
- add an `APP_PASSWORD` **KEY** with the global password as a **VALUE**
