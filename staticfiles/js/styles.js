const styles = {
  root: {
    '--primary-color': '#2D3748',
    '--secondary-color': '#4A90E2',
    '--accent-color': '#E2E8F0',
    '--background-color': '#F7FAFC',
    '--text-color': '#1A202C',
    '--border-color': '#E2E8F0',
    '--error-color': '#F56565',
    '--font-size-small': '0.875rem',
    '--font-size-medium': '1rem',
    '--font-size-large': '1.25rem',
    '--font-size-xlarge': '1.5rem',
    '--font-size-xxlarge': '2rem',
    '--spacing-xs': '0.5rem',
    '--spacing-sm': '1rem',
    '--spacing-md': '1.5rem',
    '--spacing-lg': '2rem',
    '--spacing-xl': '3rem',
    '--border-radius-small': '4px',
    '--border-radius-medium': '8px',
    '--border-radius-large': '16px',
  },
  global: {
    boxSizing: 'border-box',
    margin: 0,
    padding: 0,
    fontFamily: "'Arial', sans-serif",
    color: 'inherit',
    textDecoration: 'none',
    listStyle: 'none',
  },
  hidden: {
    display: 'none',
  },
  body: {
    fontFamily: "'Arial', sans-serif",
    backgroundColor: 'var(--background-color)',
    color: 'var(--text-color)',
    fontSize: 'var(--font-size-medium)',
    lineHeight: 1.5,
    margin: 0,
    padding: 0,
  },
  modalDialogLgCustom: {
    maxWidth: '100%',
    maxHeight: '100%',
    marginTop: '-1rem',
    border: '1px solid var(--secondary-color)',
    borderRadius: 'none',
  },
  personalInfoContent: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '20px',
  },
  residenceInfoContent: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '20px',
  },
  mb3: {
    flex: '1 1 48%',
    minWidth: '200px',
  },
  formLabel: {
    fontWeight: 'bold',
  },
  modalContent: {
    padding: '20px',
  },
  modalLgCustom: {
    maxWidth: '80%',
  },
};

export default styles;
