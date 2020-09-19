import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('renders search input', () => {
  const { getByRole } = render(<App />);
  const searchInput = getByRole('textbox');
  expect(searchInput).toBeInTheDocument();
});
