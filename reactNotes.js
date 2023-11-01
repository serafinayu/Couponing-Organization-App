// REACT tutorial tips:
// Classes: specify html element class names with className = "something"
// JS in HTML must be within curly braces: return <h1> {user.name} </h1> | string concatenation: {"Hello " + user.name}
// Styling in JSX: style={{width: user.imageSize}}
// Conditional rendering: if (isLoggedIn) { content = <AdminPanel />; } else { content = <LoginForm />; } return <div> {content} </div>
    // Shorter vers w/ if else: <div> {isLoggedIn ? ( <AdminPanel /> ) : ( <LoginForm /> )} </div>
    // Shorter vers no else: <div> {isLoggedIn && <AdminPanel />} </div>
// map() to transform array of items into li items, make sure to use a key that uniquely identifies each item (ex: <li key={product.id}> {product.name} </li>)
// Event handlers can be made in React components
// To manage state, do: import {useState} from 'react'
    // State convention: const [something, setSomething] = useState(0);
// Hooks are identified with the word "use" before a function name
    // Can only be called at the top of a component
    // They let you use state and other React functions without creating a class
    