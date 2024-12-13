import streamlit as st
from src.utils.visualization import create_confidence_gauge, create_key_features_chart

def render_results(results):
    if not results:
        return

    prediction = results['prediction']
    confidence = results['confidence']
    features = results.get('features', None)

    # Create columns for layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            f'''
            <div class="prediction-box prediction-{prediction.lower()}">
                <h2>Prediction: {prediction}</h2>
                <div class="confidence">Confidence: {confidence:.2f}%</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with col2:
        # Display confidence gauge
        create_confidence_gauge(confidence)

    # Display feature importance if available
    if features:
        st.markdown("### Key Features")
        create_key_features_chart(features)