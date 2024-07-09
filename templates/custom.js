// custom-layout.js
const CustomLayoutPlugin = (system) => {
    return {
      wrapComponents: {
        BaseLayout: (Original) => (props) => {
          // Here you can add custom HTML or wrap the Original component
          return (
            <div>
              <header>
                <h1>My Custom E-commerce API Documentation</h1>
              </header>
              <Original {...props} />
              <footer>
                <p>© 2024 E-commerce Service</p>
              </footer>
            </div>
          )
        }
      }
    }
  }