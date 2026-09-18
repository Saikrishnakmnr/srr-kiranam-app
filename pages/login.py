import streamlit as st

from services.supabase_client import get_supabase
from components.ui import inject_css, header, footer


st.set_page_config(
    page_title="Sign In",
    page_icon="🔐",
    layout="wide",
)

inject_css()
header()

supabase = get_supabase()

st.markdown(
    """
    <div class="neon-card" style="max-width:520px;margin:40px auto;padding:30px;">
        <h1 style="text-align:center;">🔐 Welcome Back</h1>
        <p style="text-align:center;opacity:.75;">
            Sign in to continue shopping
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2 = st.tabs(["📧 Sign In", "🆕 Create Account"])


with tab1:
    email = st.text_input(
        "Email",
        placeholder="Enter your email",
        key="login_email",
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
        key="login_password",
    )

    if st.button(
        "🔐 Sign In",
        use_container_width=True,
        type="primary",
    ):
        if not email or not password:
            st.warning("Please enter your email and password.")

        elif supabase is None:
            st.error("Supabase is not configured in Streamlit Secrets.")

        else:
            try:
                result = supabase.auth.sign_in_with_password(
                    {
                        "email": email,
                        "password": password,
                    }
                )

                if result.user:
                    st.session_state["user"] = result.user
                    st.success("Signed in successfully!")
                    st.rerun()

            except Exception as e:
                st.error(f"Sign in failed: {e}")


with tab2:
    name = st.text_input(
        "Full Name",
        placeholder="Your name",
        key="signup_name",
    )

    email2 = st.text_input(
        "Email",
        placeholder="Enter your email",
        key="signup_email",
    )

    password2 = st.text_input(
        "Password",
        type="password",
        placeholder="Create a password",
        key="signup_password",
    )

    password3 = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Repeat your password",
        key="signup_confirm",
    )

    if st.button(
        "🆕 Create Account",
        use_container_width=True,
        type="primary",
    ):
        if not name or not email2 or not password2:
            st.warning("Please fill in all required fields.")

        elif password2 != password3:
            st.error("Passwords do not match.")

        elif len(password2) < 6:
            st.error("Password must contain at least 6 characters.")

        elif supabase is None:
            st.error("Supabase is not configured in Streamlit Secrets.")

        else:
            try:
                result = supabase.auth.sign_up(
                    {
                        "email": email2,
                        "password": password2,
                        "options": {
                            "data": {
                                "full_name": name,
                            }
                        },
                    }
                )

                if result.user:
                    st.success(
                        "Account created successfully!"
                    )
                    st.info(
                        "If email confirmation is enabled, "
                        "please check your email before signing in."
                    )

            except Exception as e:
                st.error(f"Account creation failed: {e}")


st.markdown(
    """
    <div style="text-align:center;margin:25px 0;opacity:.7;">
        Google sign-in will be added after email authentication
        is working correctly.
    </div>
    """,
    unsafe_allow_html=True,
)

footer()
