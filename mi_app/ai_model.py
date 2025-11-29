import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class AdvancedForecaster:
    """
    Clase para realizar pronósticos avanzados de series temporales
    utilizando modelos de Machine Learning.
    """
    def __init__(self, model_type='random_forest'):
        """
        Inicializa el pronosticador con el tipo de modelo especificado.
        
        Args:
            model_type (str): Tipo de modelo a utilizar ('random_forest' o 'gradient_boosting')
        """
        self.model = None
        self.model_type = model_type
        self.model_path = os.path.join(os.path.dirname(__file__), 'forecast_model.joblib')
        self.model = self.create_model()
        self.load_model()
    
    def create_model(self):
        """Crea un nuevo modelo según el tipo especificado"""
        if self.model_type == 'gradient_boosting':
            return GradientBoostingRegressor(
                n_estimators=200,
                learning_rate=0.1,
                max_depth=5,
                random_state=42
            )
        else:  # random_forest por defecto
            return RandomForestRegressor(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                n_jobs=-1
            )
    
    def load_model(self):
        """Carga el modelo si existe, o crea uno nuevo"""
        if os.path.exists(self.model_path):
            try:
                self.model = joblib.load(self.model_path)
            except:
                self.model = self.create_model()
        else:
            self.model = self.create_model()
    
    def save_model(self):
        """Guarda el modelo en disco"""
        joblib.dump(self.model, self.model_path)
    
    def _preprocess_data(self, df):
        """Preprocesa los datos para el análisis"""
        if df.empty:
            return self._generate_sample_data(30)  # Datos de ejemplo si no hay datos reales
            
        # Convertir fechas
        if 'fecha' in df.columns:
            df['fecha'] = pd.to_datetime(df['fecha'])
            df.set_index('fecha', inplace=True)
            df.sort_index(inplace=True)  # Asegurar que esté ordenado por fecha
            
        # Asegurar que tenemos la columna de ventas
        if 'ventas' not in df.columns:
            df['ventas'] = df.get('cantidad', df.get('total', 100))
            
        # Manejar valores faltantes
        df.fillna(method='ffill', inplace=True)  # Llenar con el valor anterior
        df.fillna(method='bfill', inplace=True)  # Llenar con el siguiente valor si no hay anterior
        df.fillna(0, inplace=True)  # Llenar los restantes con 0
        
        return df
    
    def _generate_sample_data(self, days):
        """Genera datos de ejemplo para pruebas"""
        dates = pd.date_range(end=datetime.now(), periods=days)
        data = {
            'fecha': dates,
            'ventas': [100 + i*2 + random.randint(-10, 10) for i in range(days)],
            'ingresos': [1000 + i*20 + random.uniform(-100, 100) for i in range(days)],
            'clientes': [50 + i + random.randint(-5, 5) for i in range(days)],
        }
        df = pd.DataFrame(data)
        return self._preprocess_data(df)
    
    def get_daily_metrics(self):
        """Obtiene métricas diarias para el dashboard"""
        df = self.get_sales_data(30)  # Últimos 30 días
        if df.empty:
            return {}
            
        return {
            'ventas_hoy': int(df['ventas'].iloc[-1]),
            'ingresos_hoy': round(float(df['ingresos'].iloc[-1]), 2),
            'clientes_hoy': int(df['clientes'].iloc[-1]),
            'tendencia_ventas': self._calculate_trend(df, 'ventas')
        }
    
    def _calculate_trend(self, df, column):
        """Calcula la tendencia de una métrica"""
        if len(df) < 2:
            return 0
        return round(((df[column].iloc[-1] / df[column].iloc[-2]) - 1) * 100, 2)
    
    def train_forecast_model(self):
        """Entrena el modelo de pronóstico avanzado"""
        try:
            # Obtener datos históricos
            df = self.get_sales_data(365)  # Último año de datos
            
            if df.empty or len(df) < 30:  # Mínimo 30 días de datos
                return {
                    'status': 'error',
                    'message': 'No hay suficientes datos para entrenar el modelo (mínimo 30 días)'
                }
            
            # Asegurar que tenemos la columna de ventas
            if 'ventas' not in df.columns:
                df['ventas'] = df.get('cantidad', 100)
            
            # Entrenar modelo
            result = self.forecaster.train(df)
            
            # Asegurar que el resultado tenga el formato esperado
            if 'status' not in result:
                result = {
                    'status': 'success',
                    'mae': result.get('mae', 0),
                    'rmse': result.get('rmse', 0),
                    'model_type': result.get('model_type', 'random_forest')
                }
            
            return result
            
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
    
    def get_forecast(self, days_ahead=7):
        """Obtiene pronósticos avanzados"""
        try:
            # Obtener datos históricos
            df = self.get_sales_data(90)  # Últimos 90 días
            
            if df.empty or len(df) < 7:  # Mínimo 7 días de datos
                # Datos de ejemplo si no hay suficientes datos
                return [{
                    'fecha': (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'),
                    'ventas_estimadas': round(100 * (1 + i * 0.1), 2),
                    'es_simulado': True
                } for i in range(1, days_ahead + 1)]
            
            # Asegurar que tenemos la columna de ventas
            if 'ventas' not in df.columns:
                df['ventas'] = df.get('cantidad', 100)
            
            # Obtener pronóstico
            predictions = self.forecaster.predict(df, days_ahead)
            
            # Asegurar que todas las predicciones tengan el formato correcto
            for pred in predictions:
                if 'fecha' not in pred:
                    pred['fecha'] = (datetime.now() + timedelta(days=len(predictions))).strftime('%Y-%m-%d')
                if 'ventas_estimadas' not in pred:
                    pred['ventas_estimadas'] = 0
                pred['es_simulado'] = False
                
            return predictions
            
        except Exception as e:
            # En caso de error, devolver predicciones simuladas
            return [{
                'fecha': (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'),
                'ventas_estimadas': round(100 * (1 + i * 0.1), 2),
                'es_simulado': True,
                'error': str(e)
            } for i in range(1, days_ahead + 1)]