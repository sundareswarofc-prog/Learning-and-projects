import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { prevStep, resetForm } from "../Redux/store";

function ReviewSubmit() {
  const dispatch = useDispatch();
  const data = useSelector((state) => state.form.data);
  console.log('data', data)

  const handleSubmit = () => {
    alert("Form Submitted ✅\n" + JSON.stringify(data, null, 2));
    dispatch(resetForm());
  };

  return (
    <div>
      <h2>Step 3: Review & Submit</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
      <button onClick={() => dispatch(prevStep())}>Back</button>
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default ReviewSubmit;
