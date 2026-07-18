import React from "react";
import { useSelector } from "react-redux";
import PersonalInfo from "./Components/personalInfo";
import ReviewSubmit from "./Components/reviewSubmit";
import AddressInfo  from "./Components/addressInfo";

function App() {
  const step = useSelector((state) => state.form.step);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Multi-Step Form</h1>
      {step === 1 && <PersonalInfo />}
      {step === 2 && <AddressInfo />}
      {step === 3 && <ReviewSubmit />}
    </div>
  );
}

export default App;
