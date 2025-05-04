import { render, screen } from '@testing-library/react';
import App from './app';
import { describe, it, expect } from 'vitest';

describe('App component', () => {
  it('displays the welcome message', () => {
    render(<App />);

    const welcomeText = screen.getByText(/welcome to terrafy/i);

    expect(welcomeText).toBeTruthy();
  });
});
