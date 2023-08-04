"use client"
import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function Main() {
  // Step 1: Initialize react-hook-form
  const { handleSubmit, register, errors,watch } = useForm();

  // Step 2: Create a function to handle form submission
  const onSubmit = async (data) => {
      
      console.log(data)
      const username = data.username
      const password = data.password
      const finalData = {'username': username, 'password': password}
      
      try {
       
        const response = await axios.post('http://192.168.33.81:8000/auth/register/', finalData);
        console.log('Form submitted successfully!', response.data);
        toast.success('user account created successfully')
      } catch (error) {
        console.error('Error submitting form:', error);
        toast.error('error during the creation of the user')

      }

  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-base-200">
      <div className="hero min-h-screen max-w-4xl">
        <div className="hero-content flex-col lg:flex-row-reverse">
          <div className="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <div className="card-body">
                <h2 className='text-base-content font-semibold text-center'>Register</h2>
              {/* Step 4: Add the form element and attach the onSubmit handler */}
              <form onSubmit={handleSubmit(onSubmit)}>
                <div className="form-control">
                  <label className="label">
                    <span className="label-text">username</span>
                  </label>
                  {/* Step 5: Add the ref and validation rules to the input */}
                  <input
                    type="text"
                    name="username" // Set the name to match the key in the form data
                    placeholder="username"
                    className={`input input-bordered ${errors?.username ? 'input-error' : ''}`}
                    {...register('username',{ required: 'username is required' })}
                  />
                  {/* Step 6: Show error message if validation fails */}
                  {errors?.username && <span className="text-xs text-error">{errors?.username.message}</span>}
                </div>
                <div className="form-control">
                  <label className="label">
                    <span className="label-text">Password</span>
                  </label>
                  {/* Repeat Step 5 and Step 6 for other input fields */}
                  <input
                    type="password"
                    name="password"
                    placeholder="password"
                    className={`input input-bordered ${errors?.password ? 'input-error' : ''}`}
                    {...register('password',{ required: 'Password is required' })}
                  />
                  <label className="label">
                    <span className="label-text">Password Confirm</span>
                  </label>
                  <input
                    type="password"
                    name="passwordConfirm"
                    placeholder="password"
                    className={`input input-bordered ${errors?.passwordConfirm ? 'input-error' : ''}`}
                    {...register('confirm',{
                      required: 'Please confirm your password',
                      validate: (value) => value === watch('password') || 'Passwords do not match',
                    })}
                  />
                  {errors?.passwordConfirm && (
                    <span className="text-xs text-error">{errors?.passwordConfirm.message}</span>
                  )}
                  <label className="label">
                    <a href="#" className="label-text-alt link link-hover">
                      Forgot password?
                    </a>
                  </label>
                </div>
                <div className="form-control mt-6">
                  {/* Step 7: Add the submit button */}
                  <button type="submit" className="btn btn-primary">
                    Create account
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <ToastContainer autoClose={500} />
    </div>
  );
}
