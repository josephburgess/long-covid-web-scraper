import React from 'react';
import Lottie from 'lottie-react';
import loadingAnimation from '../../assets/loadingAnimation.json';
import styles from './Loading.module.css';

const Loading: React.FC = () => {
  return (
    <div className={styles.loadingContainer}>
      <div className={styles.loadingAnimationContainer}>
        <Lottie animationData={loadingAnimation} loop={true} />
      </div>
    </div>
  );
};

export default Loading;
