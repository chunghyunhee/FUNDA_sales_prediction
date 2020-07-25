# sma amount in dataframe
def make_sma_arr(window_num):
  ma_arr = np.array([]) # moving average에 해당하는 A_i값의 평균값 저장 array, return vlaue

  for i in df_month.store_id.unique():
    df_set = df_month[df_month.store_id == i] # 마찬가지로 store_id에 따라 묶어서 진행
    ma_arr = np.concatenate((ma_arr, df_set.amount.rolling(window=window_num).mean().values))
  return ma_arr


# rolling에 대한 t시점의 평균을 지정한 window에 따라 average를 설정해야 한다.
# amount값을 조정하여 잎의 3달의 값을 예측한다
def make_minus_rolling(data_frame, rolling_num):
    def minus_shift_rolling(df_num, num):
        a = np.average(df_num.values[-num:])
        b = np.average(np.append(df_set.values[-(num - 1):], a))
        if num > 2:
            c = np.average(np.append(np.append(df_set.values[-(num - 2):], a), b))
        else:
            c = np.average((a, b))
        return np.sum((a, b, c))

    minus_rolling_arr = np.array([])
    for i in data_frame.store_id.unique():
        df_set = pd.DataFrame(data_frame[data_frame.store_id == i].amount)
        minus_rolling_arr = np.concatenate((minus_rolling_arr, np.array([minus_shift_rolling(df_set, rolling_num)])))

    submission['amount'] = minus_rolling_arr
    df_rolling = submission

    return df_rolling