def get_component_styles():
    return """
        /* Header styling */
        .main-header {
            background-color: var(--bg-secondary);
            color: var(--text-primary);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        
        /* Input containers */
        .input-section {
            background-color: var(--bg-secondary);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            border: 1px solid var(--border-color);
        }
        
        .input-label {
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
            font-weight: 500;
        }
        
        /* Text area styling */
        .stTextArea textarea {
            background-color: var(--bg-secondary);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1rem;
            font-size: 1rem;
            transition: all 0.2s ease;
        }
        
        .stTextArea textarea:focus {
            border-color: var(--accent-color);
            box-shadow: 0 0 0 2px rgba(33, 150, 243, 0.1);
        }
        
        /* File uploader styling */
        .uploadfile {
            background-color: var(--bg-secondary);
            border: 2px dashed var(--border-color);
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            color: var(--text-primary);
            transition: all 0.2s ease;
        }
        
        .uploadfile:hover {
            border-color: var(--accent-color);
        }
        
        /* Button styling */
        .stButton > button {
            background-color: var(--accent-color) !important;
            color: white !important;
            padding: 0.75rem 2rem !important;
            border: none !important;
            border-radius: 8px !important;
            font-size: 1.1rem !important;
            font-weight: 500 !important;
            width: 100% !important;
            margin-top: 1rem !important;
            transition: all 0.2s ease !important;
        }
        
        .stButton > button:hover {
            opacity: 0.9 !important;
            transform: translateY(-1px) !important;
        }
        
        /* Results section */
        .results-container {
            background-color: var(--bg-secondary);
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 2rem;
            border: 1px solid var(--border-color);
        }
        
        /* Metrics cards */
        .metric-card {
            background-color: var(--bg-primary);
            border-radius: 8px;
            padding: 1rem;
            border: 1px solid var(--border-color);
        }
        
        /* Recent analysis section */
        .history-section {
            background-color: var(--bg-secondary);
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 2rem;
            border: 1px solid var(--border-color);
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .main-header {
                padding: 1rem;
            }
            
            .input-section {
                padding: 1rem;
            }
            
            .stButton > button {
                padding: 0.5rem 1.5rem !important;
            }
        }
    """