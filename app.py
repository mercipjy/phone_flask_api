from diary import create_app

# Create App
app = create_app()



# Flask 앱 가동(run)
if __name__ == "__main__":
    app.run(debug=True)