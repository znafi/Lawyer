import React, { useState, useEffect } from 'react';
import {
  Container,
  Box,
  Typography,
  TextField,
  Button,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Paper,
  CircularProgress,
  Card,
  CardContent,
  Stepper,
  Step,
  StepLabel,
  IconButton,
  Chip,
  Divider,
  useTheme,
  alpha
} from '@mui/material';
import {
  Search as SearchIcon,
  Language as LanguageIcon,
  Public as PublicIcon,
  Gavel as GavelIcon,
  NavigateNext as NavigateNextIcon,
  NavigateBefore as NavigateBeforeIcon
} from '@mui/icons-material';
import axios from 'axios';

// Use relative URL in production, localhost in development
const API_BASE_URL = process.env.NODE_ENV === 'production' ? '/api' : 'http://localhost:5000/api';

function App() {
  const theme = useTheme();
  const [languages, setLanguages] = useState([]);
  const [countries, setCountries] = useState([]);
  const [selectedLanguage, setSelectedLanguage] = useState('');
  const [selectedCountry, setSelectedCountry] = useState('');
  const [keywords, setKeywords] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState(0);

  useEffect(() => {
    fetchLanguages();
    fetchCountries();
  }, []);

  const fetchLanguages = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/languages`);
      setLanguages(response.data);
    } catch (error) {
      console.error('Error fetching languages:', error);
    }
  };

  const fetchCountries = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/countries`);
      setCountries(response.data);
    } catch (error) {
      console.error('Error fetching countries:', error);
    }
  };

  const handleSearch = async () => {
    setLoading(true);
    try {
      console.log('Searching with:', { selectedCountry, keywords, selectedLanguage });
      const response = await axios.get(`${API_BASE_URL}/laws/search`, {
        params: {
          country_id: selectedCountry,
          keywords,
          language: selectedLanguage
        }
      });
      console.log('Search response:', response.data);
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error searching laws:', error);
    }
    setLoading(false);
  };

  const handleNext = () => {
    setStep((prevStep) => prevStep + 1);
  };

  const handleBack = () => {
    setStep((prevStep) => prevStep - 1);
  };

  const steps = ['Select Language', 'Choose Country', 'Search Laws'];

  const renderStepContent = (stepIndex) => {
    switch (stepIndex) {
      case 0:
        return (
          <Box sx={{ mt: 4, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <LanguageIcon sx={{ fontSize: 60, color: theme.palette.primary.main, mb: 2 }} />
            <Typography variant="h5" gutterBottom align="center" sx={{ mb: 3 }}>
              Select Your Language
            </Typography>
            <FormControl 
              fullWidth 
              sx={{ 
                maxWidth: 400,
                '& .MuiOutlinedInput-root': {
                  borderRadius: 2
                }
              }}
            >
              <InputLabel>Language</InputLabel>
              <Select
                value={selectedLanguage}
                onChange={(e) => setSelectedLanguage(e.target.value)}
                sx={{ bgcolor: 'background.paper' }}
              >
                {languages.map((lang) => (
                  <MenuItem key={lang.code} value={lang.code}>
                    {lang.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
        );
      case 1:
        return (
          <Box sx={{ mt: 4, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <PublicIcon sx={{ fontSize: 60, color: theme.palette.primary.main, mb: 2 }} />
            <Typography variant="h5" gutterBottom align="center" sx={{ mb: 3 }}>
              Choose Your Country
            </Typography>
            <FormControl 
              fullWidth 
              sx={{ 
                maxWidth: 400,
                '& .MuiOutlinedInput-root': {
                  borderRadius: 2
                }
              }}
            >
              <InputLabel>Country</InputLabel>
              <Select
                value={selectedCountry}
                onChange={(e) => setSelectedCountry(e.target.value)}
                sx={{ bgcolor: 'background.paper' }}
              >
                {countries.map((country) => (
                  <MenuItem key={country.id} value={country.id}>
                    {country.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
        );
      case 2:
        return (
          <Box sx={{ mt: 4 }}>
            <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mb: 4 }}>
              <GavelIcon sx={{ fontSize: 60, color: theme.palette.primary.main, mb: 2 }} />
              <Typography variant="h5" gutterBottom align="center">
                Search Laws
              </Typography>
            </Box>
            <Box sx={{ display: 'flex', alignItems: 'center', maxWidth: 600, mx: 'auto' }}>
              <TextField
                fullWidth
                label="Enter keywords to search laws"
                value={keywords}
                onChange={(e) => setKeywords(e.target.value)}
                sx={{
                  '& .MuiOutlinedInput-root': {
                    borderRadius: 2,
                    bgcolor: 'background.paper'
                  }
                }}
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    handleSearch();
                  }
                }}
              />
              <IconButton 
                onClick={handleSearch}
                sx={{ 
                  ml: 1,
                  bgcolor: theme.palette.primary.main,
                  color: 'white',
                  '&:hover': {
                    bgcolor: theme.palette.primary.dark
                  }
                }}
              >
                <SearchIcon />
              </IconButton>
            </Box>
            {loading ? (
              <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
                <CircularProgress />
              </Box>
            ) : (
              <Box sx={{ mt: 4 }}>
                {searchResults.map((law) => (
                  <Card 
                    key={law.id} 
                    sx={{ 
                      mb: 2,
                      borderRadius: 2,
                      boxShadow: theme.shadows[3],
                      '&:hover': {
                        boxShadow: theme.shadows[6],
                        transform: 'translateY(-2px)',
                        transition: 'all 0.3s ease-in-out'
                      }
                    }}
                  >
                    <CardContent>
                      <Typography variant="h6" gutterBottom color="primary">
                        {law.title}
                      </Typography>
                      <Box sx={{ display: 'flex', gap: 1, mb: 2, flexWrap: 'wrap' }}>
                        <Chip 
                          label={`Source: ${law.source}`}
                          size="small"
                          sx={{ bgcolor: alpha(theme.palette.primary.main, 0.1) }}
                        />
                        <Chip 
                          label={`Section: ${law.section}`}
                          size="small"
                          sx={{ bgcolor: alpha(theme.palette.secondary.main, 0.1) }}
                        />
                        <Chip 
                          label={`Year: ${law.year}`}
                          size="small"
                          sx={{ bgcolor: alpha(theme.palette.info.main, 0.1) }}
                        />
                      </Box>
                      <Divider sx={{ my: 2 }} />
                      <Typography variant="body1" sx={{ whiteSpace: 'pre-line' }}>
                        {law.content}
                      </Typography>
                    </CardContent>
                  </Card>
                ))}
              </Box>
            )}
          </Box>
        );
      default:
        return null;
    }
  };

  return (
    <Box 
      sx={{ 
        minHeight: '100vh',
        bgcolor: '#f5f7fa',
        pt: 4,
        pb: 8
      }}
    >
      <Container maxWidth="lg">
        <Box sx={{ mb: 6, textAlign: 'center' }}>
          <Typography 
            variant="h3" 
            component="h1" 
            gutterBottom 
            sx={{ 
              fontWeight: 700,
              background: `linear-gradient(45deg, ${theme.palette.primary.main}, ${theme.palette.secondary.main})`,
              backgroundClip: 'text',
              textFillColor: 'transparent',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent'
            }}
          >
            Global Legal Reference System
          </Typography>
          <Typography variant="h6" color="text.secondary">
            Your comprehensive guide to legal information worldwide
          </Typography>
        </Box>

        <Paper 
          sx={{ 
            p: 4,
            borderRadius: 3,
            boxShadow: theme.shadows[3],
            bgcolor: alpha('#fff', 0.9),
            backdropFilter: 'blur(20px)'
          }}
        >
          <Stepper activeStep={step} alternativeLabel>
            {steps.map((label) => (
              <Step key={label}>
                <StepLabel>{label}</StepLabel>
              </Step>
            ))}
          </Stepper>

          {renderStepContent(step)}

          <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 4 }}>
            <Button
              onClick={handleBack}
              disabled={step === 0}
              startIcon={<NavigateBeforeIcon />}
              sx={{ 
                visibility: step === 0 ? 'hidden' : 'visible',
                borderRadius: 2
              }}
            >
              Back
            </Button>
            <Button
              variant="contained"
              onClick={step === steps.length - 1 ? handleSearch : handleNext}
              disabled={(step === 0 && !selectedLanguage) || (step === 1 && !selectedCountry)}
              endIcon={step === steps.length - 1 ? <SearchIcon /> : <NavigateNextIcon />}
              sx={{ 
                visibility: step === steps.length - 1 ? 'hidden' : 'visible',
                borderRadius: 2
              }}
            >
              {step === steps.length - 1 ? 'Search' : 'Next'}
            </Button>
          </Box>
        </Paper>
      </Container>
    </Box>
  );
}

export default App;
