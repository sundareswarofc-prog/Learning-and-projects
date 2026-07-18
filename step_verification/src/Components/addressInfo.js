import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateForm, nextStep, prevStep } from "../Redux/store";

function AddressInfo() {
  const dispatch = useDispatch();
  const { address, city } = useSelector((state) => state.form.data);

  const handleChange = (e) => {
    dispatch(updateForm({ [e.target.name]: e.target.value }));
  };

  return (
    <div>
      <h2>Step 2: Address Info</h2>
      <input name="address" value={address} onChange={handleChange} placeholder="Address" />
      <input name="city" value={city} onChange={handleChange} placeholder="City" />
      <button onClick={() => dispatch(prevStep())}>Back</button>
      <button onClick={() => dispatch(nextStep())}>Next</button>
    </div>
  );
}

export default AddressInfo;
