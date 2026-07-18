import logo from './logo.svg';
import './App.css';
import { CheckoutForm } from './checkoutForm';
import { loadStripe } from "@stripe/stripe-js";
import {
  Elements
} from "@stripe/react-stripe-js";


const stripePromise = loadStripe("pk_test_51S6nPWCbQkKJHanDFTAyl3Mxp9Kfhzanbd2azSfEZWhRxJN3CUJG2lYocglnMQaWHL3fkzynKo28B4LiLScGIjUA005VW1TBC9");

function App() {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm/>
    </Elements>
  );
}

export default App;
